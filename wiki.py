def Wikipedia(command, engine):
    import wikipedia
    import time 

    query = command.replace("wikipedia", "")
    engine(f'searching wikipedia for {query}....')
    try:
        sentences = int(input("Please enter the no. of sentenses you want on the particular topic :-\t"))
        result = wikipedia.summary(query, sentences=sentences)
        engine("according to wikipedia")
        print(result)
        engine(result)
        time.sleep(7)
    except:
        engine("no search query was given")
