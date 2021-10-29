#!/usr/bin/python3
import urllib.request, argparse
import time, datetime

def dl_jpg(url, filepath, filename):
    fullpath = filepath + filename
    urllib.request.urlretrieve(url, fullpath)

def main():
    # Create a parser
    parser = argparse.ArgumentParser(prog='ImagePipe', description='A useful tool for following periodic changes on websites and downloading images.')

    # Add positional arguments
    parser.add_argument('url', type=str, nargs=1, metavar='url', default=None, help='URL to the website containing the image')
    
    # Add optional arguments
    parser.add_argument('-i', '--interval', type=int, nargs=1, metavar='time', default=None, help='Time interval in seconds for downloading images')
    parser.add_argument('-f', '--filename', type=str, nargs=1, metavar='fname', default=None, help='Name with which to sign a file')
    parser.add_argument('-p', '--path', type=str, nargs=1, metavar='path', default='./', help='Path to the save file location')

    # Parse arguments and convert them into variables
    args = parser.parse_args()
    
    url = args.url[0]
    path = args.path[0] + '/'

    if args.interval != None:
        interval = args.interval[0]

    # Add some headers for spoofing the site
    opener=urllib.request.build_opener()
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)

    while True:
        # Make a filename
        month = str(datetime.datetime.now().month)
        day = str(datetime.datetime.now().day)
        hour = str(datetime.datetime.now().hour)
        minute = str(datetime.datetime.now().minute)
        second = str(datetime.datetime.now().second)

        filename = month + '.' + day + '_' + hour + '.' + minute + '.' + second + '.jpg'

        # Download the image and sleep for a given time
        dl_jpg(url, path, filename)

        if args.interval != None:
            time.sleep(interval)
        else:
            break

# Call the main function
if __name__ == '__main__':
    main()