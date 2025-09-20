import os


def delete():
    path = os.environ["APPDATA"] + "\\" + "Typora"
    if os.path.exists(path):
        for dirpath, dirnames, filenames in os.walk(path, topdown=False):
            for name in filenames:
                print("Removing file: " + os.path.join(dirpath, name))
                os.remove(os.path.join(dirpath, name))
            for name in dirnames:
                print("Removing dir: " + os.path.join(dirpath, name))
                os.rmdir(os.path.join(dirpath, name))
        os.rmdir(path)


if __name__ == "__main__":
    delete()
