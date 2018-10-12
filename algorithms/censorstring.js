function censorstring(strMain, strWord) {
    var xChar = "x";
    var strCensored = xChar.repeat(strWord.length);
    var strNew = "";
    var strTemp = "";

    for (i = 0; i < strMain.length; i++) {
        console.log(i);
        var bFoundMatch = true;
        if (strMain[i] == strWord[0]) {
            strTemp = strWord[0];
            for (j = 1; bFoundMatch && j < strWord.length; j++) {
                console.log(strMain[i + j] == strWord[j])
                console.log((i + j) + "  " + strMain[i + j]);
                bFoundMatch = bFoundMatch && (strMain[i + j] == strWord[j])
                strTemp += strMain[i + j - 1];

            }

            if (bFoundMatch) {
                console.log("bFoundMatch==TRUE => " + strTemp)
                strNew += strCensored;
            } else {
                strTemp += strMain[i + j - 1];
                console.log("bFoundMatch==FALSE => " + strTemp)
                strNew += strTemp;
            }

            console.log(strNew);
            strTemp = "";
            i += --j;
        }
        strNew += strMain[i];
        console.log(strNew);
    }
    return strNew;
}

console.log(censorstring("nincompool", "poop"));