import socket
import tkinter as tk
from tkinter import messagebox

def scan_ports():
    target = entry_target.get()
    try:
        start_port = int(entry_start.get())
        end_port = int(entry_end.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter valid port numbers")
        return
    
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Starting scan on {target} from port {start_port} to {end_port}...\n")
    
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
            result_text.insert(tk.END, f"Port {port} is OPEN\n")
        sock.close()
    result_text.insert(tk.END, "Scan finished.\n")

root = tk.Tk()
root.title("Port Scanner")

tk.Label(root, text="Enter IP or Domain:").pack()
entry_target = tk.Entry(root, width=30)
entry_target.pack()

tk.Label(root, text="Start Port:").pack()
entry_start = tk.Entry(root, width=10)
entry_start.pack()

tk.Label(root, text="End Port:").pack()
entry_end = tk.Entry(root, width=10)
entry_end.pack()

scan_button = tk.Button(root, text="Start Scan", command=scan_ports)
scan_button.pack()

result_text = tk.Text(root, height=15, width=50)
result_text.pack()
