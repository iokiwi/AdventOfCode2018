def main():	
    i = input()
    values = []
    while(i):
        try: 
            values.append(i)
            i = input()
        except EOFError:
            break

    answer = reduce(lambda x, y: x+y, values)
    print(answer)

if __name__ == "__main__":
	main()