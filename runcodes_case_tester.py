import os

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    filename = input("Insira o nome do arquivo:\n")
    in_files = sorted(f for f in os.listdir(path) if f.endswith('.in'))
    out_files = sorted(f for f in os.listdir(path) if f.endswith('.out'))
    
    test_cases = []
    for in_file in in_files:
        base_name = in_file[:-3]
        out_file = base_name + '.out'
        if out_file in out_files:
            test_cases.append((in_file, out_file))
    
    for in_file, out_file in test_cases:
        print(f"\n{'='*40}")
        print(f"TESTE: {in_file[:-3]}")
        print(f"{'='*40}")
        
        print("Sua saída:")
        infile_path = os.path.join(path, in_file)
        os.system(f"{filename} < \"{infile_path}\"")
        
        print(f"\nSaída esperada:")
        outfile_path = os.path.join(path, out_file)
        os.system(f"cat \"{outfile_path}\"")
        print()

if __name__ == "__main__":
    main()
