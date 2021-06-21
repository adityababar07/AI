def Wikipedia(command, engine):
    import wikipedia
    import time 

    query = command.replace("wikipedia", "")
    engine(f'searching wikipedia for {query}....')
    try:
        result = wikipedia.summary(query, sentences=2)
        engine("according to wikipedia")
        print(result)
        engine(result)
        time.sleep(7)
    except:
        engine("no search query was given")
