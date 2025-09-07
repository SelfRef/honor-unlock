import subprocess
import time

START_PIN = 1000000000000000
END_PIN = 9999999999999999
SAVE_EVERY = 50
LAST_PIN_FILE = 'last_pin.txt'
SUCCESS_PIN_FILE = 'success_pin.txt'

def save_last_pin(pin):
	with open(LAST_PIN_FILE, 'w') as f:
		f.write(str(pin))

def save_success_pin(pin):
	with open(SUCCESS_PIN_FILE, 'w') as f:
		f.write(str(pin))

def load_last_pin():
	try:
		with open(LAST_PIN_FILE, 'r') as f:
			return int(f.read().strip())
	except Exception:
		return START_PIN

def main():
	pin = load_last_pin()
	tries = 0
	start_time = time.time()
	while pin <= END_PIN:
		iter_start = time.time()
		cmd = ["fastboot", "oem", "unlock", str(pin)]
		try:
			result = subprocess.run(cmd, capture_output=True, text=True)
			output = result.stdout + result.stderr
		except Exception as e:
			output = str(e)
		print(f"Trying PIN: {pin}")
		if tries % SAVE_EVERY == 0:
			elapsed = time.time() - start_time
			pins_left = END_PIN - pin
			avg_time = elapsed / (tries + 1) if tries > 0 else 0.1
			est_seconds = pins_left * avg_time
			est_days = int(est_seconds // 86400)
			est_hours = int((est_seconds % 86400) // 3600)
			print(f"Estimated time left: {est_days}d {est_hours}h")
		if 'success' in output.lower():
			save_success_pin(pin)
			print(f"Success! PIN: {pin}")
			break
		tries += 1
		if tries % SAVE_EVERY == 0:
			save_last_pin(pin)
		pin += 1

if __name__ == "__main__":
	main()
