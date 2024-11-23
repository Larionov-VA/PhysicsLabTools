def inputSamples():
    samples = []
    i = 1
    print("Значения выборки печатайте поочередно в формате float, после каждого значения нажимайте Enter")
    while True:
        sample = input(f"Введите {i} значение: \n")
        if sample == "" or sample == "\t" or sample == "\n":
            print(f"Вы записали значения {samples}, прервать запись?")
            n = input("Y/N\n")
            if n == "Y":
                break
            else:
                continue
        sample = sample.replace(",",".")
        samples.append(float(sample))
        i += 1
    return samples
