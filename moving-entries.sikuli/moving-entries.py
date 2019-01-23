click(Pattern("1548237032927.png").similar(0.60))

while exists(Pattern("1548237318013.png").similar(0.85)):
    click(Pattern("1548237318013.png").similar(0.85).targetOffset(157,3))
    click(Pattern("1548237474102.png").similar(0.80))
    click(Pattern("1548237512982.png").similar(0.80))
    
    wait("1548237952159.png")
    click(Pattern("1548237952159.png").similar(0.75).targetOffset(64,-14))
    wait(Pattern("1548237318013.png").similar(0.85))
    click(Pattern("1548238041498.png").similar(0.80).targetOffset(-37,2))
    wait("1548238102442.png")
    click(Pattern("1548238102442.png").targetOffset(-45,0))
    