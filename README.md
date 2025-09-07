# Honor/Huawei Bootloader Unlock Brute-Force Script

This script attempts to brute-force the bootloader unlock code for Huawei or Honor devices using the `fastboot oem unlock <PIN>` command. It tries all 16-digit PINs starting from `1000000000000000` and saves progress every 50 attempts.

## How It Works

- The script runs `fastboot oem unlock <PIN>` for each PIN.
- Every 50 tries, it saves the last tried PIN to `last_pin.txt` so you can resume if interrupted.
- If the output contains the word `success`, the PIN is saved to `success_pin.txt` and the script stops.
- The output of each attempt is printed to the terminal.

## Usage

1. Make sure you have Python 3 installed.
2. Connect your Huawei/Honor device in fastboot mode and ensure `fastboot` is available in your PATH.
3. Run the script:

	```fish
	python unlock.py
	```

4. To resume from the last tried PIN, simply run the script again.

## Files

- `unlock.py`: The brute-force script.
- `last_pin.txt`: Stores the last tried PIN for resuming.
- `success_pin.txt`: Stores the successful unlock PIN if found.

**Warning:** Brute-forcing unlock codes may violate device terms of service and can permanently lock or damage your device. Use at your own risk.
