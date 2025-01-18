"""
UI for youtube_to_mp3. Designed to allow youtube_to_mp3 to work independently.

Not all events are shown in the event viewer. The console of the actual files still
outputs however


"""




import tkinter as tk
import youtube_to_mp3
import threading

root = tk.Tk()
root.title("YouTube to MP3")
root.resizable(False, False)

def parse_tb(urls):
    """
    Takes each url from the UI and parses it. Then
    calls the dowloader function for each URL
    """

    urls = urls.replace(" ", "")
    url_list = urls.split("\n")
    return url_list



def download():
    """
    TODO fix thread; VERBOSE
    """

    def run_yt():
        returns = []
        input = url_textbox.get("1.0", "end-1c")
        url_list = parse_tb(input)
        for url in url_list:
            display_status(url=url)

            success, error = youtube_to_mp3.youtube_to_mp3(url)
            youtube_to_mp3.clean_files()
            returns.append(success)
            returns.append(error)

            success = returns[0]
            error = returns[1]
            display_status(url=url, success=success, error=error)

            youtube_to_mp3.clean_files()



    x = threading.Thread(target=run_yt, args=())
    x.start()



def cancel():
    root.destroy()



def display_status(url, **kwargs):
    """
    Displays the status of the Download
    """

    if "success" in kwargs:
        if kwargs["success"] == True:
            message = (f"{url} Successfully Downloaded!")
        elif kwargs["success"] == False:
            message = (f"{url} ERROR: FAILED TO DOWNLOAD {kwargs['error']}")
    else:
        message = (f"{url}: Downloading...")


    message = message + "\n" + "\n"
    event_monitor.configure(state=tk.NORMAL)
    event_monitor.insert(tk.END, message)
    event_monitor.configure(state=tk.DISABLED)



def clear(text_box):
    if text_box == event_monitor:
        text_box.configure(state=tk.NORMAL)
        text_box.delete("1.0", tk.END)
        text_box.configure(state=tk.DISABLED)

    if text_box == url_textbox:
        text_box.delete("1.0", tk.END)

url_header = (tk.Label(root, text="Enter URLS below. Use a newline to separate"))
url_header.grid(row=0, column=0, columnspan=2, sticky="nesw")

em_header = tk.Label(root, text="Event Monitor")
em_header.grid(row=0, column=2, columnspan=2, sticky="nesw")

url_textbox = tk.Text(
    root,
    height = 30,
    width = 50,
)

url_textbox.grid(
    row=1,
    column=0,
    columnspan=3,
    rowspan=3,
    padx=10,
    pady=10
)

###DOWNLOAD BUTTON###

dl_button = tk.Button(
    root,
    height=2,
    width=10,
    text="Download",
    bg="#37a9fa",
    activebackground="#346c94",
    command=lambda:download()
)

dl_button.grid(
    row=4,
    column=0,
    padx=10,
    pady=10
)

###CLEAR BUTTON FOR URLS###

clear_button_urls = tk.Button(
    root,
    height=2,
    width=10,
    text="Clear",
    bg="#37a9fa",
    activebackground="#346c94",
    command=lambda:clear(url_textbox)
)

clear_button_urls.grid(
    row=4,
    column=1,
    padx=10,
    pady=10,
)

###CANCEL BUTTON###

cancel_button = tk.Button(
    root,
    height=2,
    width=10,
    text="Cancel",
    bg="#b02c39",
    activebackground="#82212a",
    command=lambda:cancel()
)

cancel_button.grid(
    row=4,
    column=2,
    padx=10,
    pady=10
)

###EVENT MONITOR###

event_monitor = tk.Text(
    root,
    height=30,
    width=50,
    state=tk.DISABLED,
    relief=tk.SUNKEN,
)


event_monitor.grid(
    row=1,
    column=3,
    columnspan=2,
    rowspan=3,
    padx=10,
    pady=10
)

###CLEAR BUTTON FOR EVENT MONITOR###

clear_button_event = tk.Button(
    root,
    height=2,
    width=10,
    text="Clear",
    bg="#b02c39",
    activebackground="#82212a",
    command=lambda:clear(event_monitor)
)

clear_button_event.grid(
    row=4,
    column=3,
    padx=10,
    pady=10,
    columnspan=2
)

root.mainloop()

