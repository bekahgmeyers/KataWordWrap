class Wrapper:

    line = "Fruitful, yielding-them don't fifth. He. To said-lesser, hath wherein sixth-midst day his fly them signs greater-man air-to-beast creature. It meat-given above brought creepeth isn't form-morning. Sixth-created green-multiply greater. Creepeth open, set can't morning brought second-open living behold-sea them. A fruit-whose, you'll grass. All every was. Every-divided also itself winged-lights meat-beast sixth-it-fifth wherein seed, their Also. Green-stars divide appear-seas His beginning there-sea that yielding saw-sixth. Kind-day male-waters male-years meat-herb he fly two-sea meat. Upon."

    def wrap(line, column):
        count = 0
        lines = ""

        for word in line.split():

            if "-" in word:
                first = word.split('-', 1)[0] + "-"
                second = word.split('-', 1)[1]

                count += len(first)

                if count > column:
                    lines = lines[:-1] + "\n"
                    count = (len(word) + 1)
                    lines += (word + " ")
                else:
                    if (count + len(second)) > column:
                        lines += (first + "\n" + second + " ")
                        count = len(second) + 1
                    else:
                        lines += (word + " ")
                        count += (len(second) + 1)
            else:
                count += len(word)

                if count > column:
                    lines = lines[:-1] + "\n"
                    count = len(word)

                lines += (word + " ")
                count += 1

        return lines

    print(wrap(line, 50))


