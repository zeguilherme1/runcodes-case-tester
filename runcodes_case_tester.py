import os

def main():
    path = os.path.dirname(os.path.abspath(__file__))

    filename = input("Insira o nome do arquivo:\n")

    in_files = sorted(f for f in os.listdir(path) if f.endswith('.in'))
    out_files = sorted(f for f in os.listdir(path) if f.endswith('.out'))

    print("\nSua saída:")
    for infile in in_files:
        infile_path = os.path.join(path, infile)
        os.system(f"{filename} < \"{infile_path}\"")
        print()

    print("-" * 20)
    print("\nSaída esperada:")
    for outfile in out_files:
        outfile_path = os.path.join(path, outfile)
        os.system(f"cat \"{outfile_path}\"")

    print()

if __name__ == "__main__":
    main()

