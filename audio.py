from soundfile import read

def main():
    (data, samplerate) = read("input.flac")
    print(data)

if __name__ == "__main__":
	main()