
def load_data():
    pass

def list_all_videos(videos):
    pass

def add_video(video):
    pass

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

     

    
