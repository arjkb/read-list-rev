import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="input file name", type=str)
    args = parser.parse_args()

    with open(args.filename) as f:
        for line in f:
            line = line.strip()
            spl = line.split('|')
            t = spl[2]
            title = t[1:t.index('(')-1]
            link = t[t.index('(')+1: t.index(')')]
            author = spl[3]
            print("{} | {} | {}".format(title, author, link))

if __name__ == '__main__':
    main()
