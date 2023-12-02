#Easy3

def Pascaltriangle(num_rows):
    tri = []

    for i in range(num_rows):
        row = [1] * (i + 1)

        for j in range(1, i):
            row[j] = tri[i-1][j-1] + tri[i-1][j]

        tri.append(row)

    return tri

def main():
    try:
        num_rows = int(input("numRows:"))
        
        if 1 <= num_rows <= 30:
            result = Pascaltriangle(num_rows)
            print(result)
        else:
            print("Invalid input, please enter a number between 1 and 30")
    except ValueError:
        print("enter a valid integer.")

if __name__ == "__main__":
    main()

