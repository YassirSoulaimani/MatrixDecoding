''' ****************************************************************
By : Yassir Soulaimani
Email: yassir.soulaimani@gmail.com

 **************************************************************** '''

from math import pow

# Global variables
codes = []       # Contains all the codewords of the given binary linear code
decodingCodes = []   # Contains all the codewords of the decoded matrix.
inputK = 0       # 'k' value of input code.
inputN = 0       # 'n' value of input code.



def generateInputCodes():
    global inputN, inputK, codes
    # Open the input file to read the Generator matrix of binary linear code [n, k]
    fid = open('input.txt', 'r')
    rows = fid.readlines()
    inputK = len(rows)
    generator_codes = []

    for i in range(0, inputK):
        code = rows[i].split()
        code = map(int, code)

        # Insert all the codes of generator matrix in codes array.
        generator_codes.append(code)

    inputN = len(generator_codes[0])

    # Generate all the cosets of the generator matrix.
    totalCodes = int(pow(2, inputK))
    for i in range(0, int(totalCodes)):
        code = inputN * [0]
        shift = 0
        while (shift != inputK):
            if ((i >> shift) & 1):
                for j in range(0, inputN):
                    code[j] += generator_codes[shift][j] % 2
            shift += 1
        codes.append(code)


# decode all the parameters and all the cosets.
def decode():
    global decodingCodes
    totalCodeSpace = int(pow(2, inputN))
    for code in range(0, totalCodeSpace):
        isOrthogonal = 1
        for inputCode in codes:
            shift = inputN - 1
            sum = 0
            while shift != -1:
                sum = (sum + inputCode[inputN - shift - 1] * ((code >> shift) & 1)) % 2
                shift -= 1
            if sum != 0:
                isOrthogonal = 0
                break

        if isOrthogonal:
            generatedCode = []
            shift = inputN - 1
            while shift != -1:
                generatedCode.append((code >> shift) & 1)
                shift -= 1
            decodingCodes.append(generatedCode)



#Write the decoding table to the output file
def writeOutputToFile():
    output_file = open('output.txt', 'w')

    output_file.write("\nThe decoding table :\n\n")
    for decodingCode in decodingCodes:
        output_file.write("(")
        for i in range(0, inputN - 1):
            output_file.write(str(decodingCode[i]) + " ")
        output_file.write(str(decodingCode[inputN - 1]) + ")\n")

#write the decoding table to the console
def output():

    print "The decoding table :\n"
    for decodingCode in decodingCodes:
        print "(",
        for i in range(0, inputN - 1):
            print str(decodingCode[i]) + "",

        print str(decodingCode[inputN - 1]) + " )"


def main():
    # Generate all the input codewords
    generateInputCodes()

    # decode all the codewords of the generator matrix codes
    decode()

    # Write all the codewords of generator matrix.
    writeOutputToFile()

    # Print the output to the standard output.
    output()


if __name__ == '__main__':
    main()