import service


def main():
    print("Welcome to the talk python info downloader")
    print()

    service.download_info()

    for show_id in range(234, 260):
        info = service.get_episode(show_id)
        print(f"{info.show_id}. {info.title}")


if __name__ == '__main__':
    main()
