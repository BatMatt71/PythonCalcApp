import options

def MathOption(nums, option):
    optionList = [options.Exit, options.Add, options.Sub, options.Mult, options.Divid, options.Modul, options.Power, options.SqrRoot]

    return optionList[option](nums)