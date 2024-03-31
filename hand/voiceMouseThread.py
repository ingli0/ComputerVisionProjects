import multiprocessing
import voiceControl
import mouseVirtual

if __name__ == "__main__":
    # Create processes for each module
    voice_control_process = multiprocessing.Process(target=voiceControl.listen_and_type)
    mouse_virtual_process = multiprocessing.Process(target=mouseVirtual.main)

    # Start the processes
    voice_control_process.start()
    mouse_virtual_process.start()

    # Wait for both processes to finish
    voice_control_process.join()
    mouse_virtual_process.join()
