# This is the Class for middle-level applicant for cover-letter builder
class MiddleLvl:
    def MiddleLevel():
        hiringManagerName = input("Hiring Manager's Name: ")
        jobTitle = input("Job Title: ")
        companyName = input("Company Name: ")
        pcJobTitle = input("Previous or Current Job Title: ")
        Number = input("Number of years of expertise: ")
        keySkills = input("Several Key Skills: ")
        jobRequirementsFromdAdvert = input(
            "Several Job Requirements From the Advert: ")
        mrcCompany = input("Most Recent or Current Company: ")
        Accomplishments = input("A Few Accomplishments: ")
        fullName = input("Full Name: ")
        phoneNumber = input("Phone Number: ")
        email = input("Email: ")

        middleLevel = f"\nDear {hiringManagerName} \
        \nWhen I came across your advertisement looking to fill the {jobTitle} position at {companyName}, \
        \nI was immediately excited. As a {pcJobTitle} having {Number} years of expertise, \
        \nI've developed and become highly skilled in {keySkills}. As such, I believe \
        \nI would make a perfect choice for the position and your company's upcoming goals \
        \nAccording to the job ad, you are trying to find a {jobTitle} with experience in {jobRequirementsFromdAdvert}.\
        \nDuring my time at {mrcCompany} as a {jobTitle}, \
        \nI succeeded in {Accomplishments}. I am sure that my experience would allow \
        \nme to effectively replicate such results at {companyName}. \
        \nCould we have a talk about how my skills and professional background can help {companyName} \
        \ncomplete its upcoming targets and deliverables? \
        \nSincerely, \
        \n{fullName} \
        \n{phoneNumber} \
        \n{email}"

        print(middleLevel)

    #MiddleLevel()
