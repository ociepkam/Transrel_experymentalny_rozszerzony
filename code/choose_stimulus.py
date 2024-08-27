def choose_stimulus(stimulus_type):
    if stimulus_type == "Latin":
        import string
        alphabet = list(string.ascii_uppercase)
        to_remove = "IQMERW"
        [alphabet.remove(elem) for elem in to_remove]
        stimulus = {"type": "text", "strict_sets": False, "stimulus_list": alphabet}
    elif stimulus_type == "Numbers":
        stimulus = {"type": "text", "strict_sets": False, "stimulus_list": [str(num) for num in range(10)]}
    elif stimulus_type == "Figures":
        stimulus = {"type": "text", "strict_sets": True,  "stimulus_list": [["■", "⬬", "◣"],
                                                                            ["◆", "⬤", "▲"],
                                                                            ["▮", "⬣", "►"],
                                                                            ["▬", "★", "▰"]]}
    else:
        raise Exception("Unknown stimulus type")
    return stimulus
