import json

x = 'youtube.txt'
def load_data():
    try:
        with open('x', 'r') as file:
            return json.load(file)  # .txt file ko json mein convert krke tab save karega
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('x', 'w') as file:
        json.dump(videos, file)  # json do imputs leta hai kya likhna hai (videos) aur kha likhna hai (file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1): #enumarate se index bna diya jo ki 1 se start hoga
        print(f"{index}. ")

def add_video(video):
    title = input ("Enter video title: ")
    length= input ("Enter video length: ")
    video.append({'title': title, 'length': length})
    save_data_helper(video)

def update_video(video):
    pass

def delete_video(video):
    pass


def main():
    videos = load_data # data file se load krega
    video = [videos()]
    while True:
        print("\n Youtube Manager... choose an option")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        print(videos)

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(video)
            case '3':
                update_video(video)
            case '4':
                delete_video(video)
            case '5':
                break
            case _:
                print("Wrong choice. Try again.")  
    
if __name__ == "__main__":
    main()  # agr khi bhi  main ho code mein toh ye run hoga 
     

    
