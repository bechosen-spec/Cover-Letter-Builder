# This is the class for senior-level applicant for cover-letter builder
class SeniorLvl:
    def SeniorLevel():
        hiringManagerName = input("Hiring Manager's Name: ")
        careerField = input("Career Field: ")
        bigAchievement = input("Big Achievement or Milestone You Attained: ")
        positionName = input("Position Name: ")
        companyName = input("Company Name: ")
        keyCompanyGoal = input("Key Company Goal or Mission: ")
        skill1 = input("Skill  No. 1: ")
        skill2 = input("Skill  No. 2: ")
        skill3 = input("Skill  No. 3: ")
        achievement1 = input(
            "Achievement  No. 1 that Used a Skill they Need: ")
        achievement2 = input(
            "Achievement  No. 2 that Used a Skill they Need: ")
        achievement3 = input(
            "Achievement  No. 3 that Used a Skill they Need: ")
        moreSkills = input("2 More Skills They Need: ")
        quotefromMissionStatement = input(
            "Quote from Company’s Mission Statement: ")
        fullName = input("Full Name: ")
        phoneNumber = input("Phone Number: ")
        email = input("Email: ")

        seniorLevel = f"Dear {hiringManagerName}, \
        Throughout the years of my professional work I've gained a lot of expertise in {careerField}. \
        I'm especially proud of {bigAchievement} which was both \
        challenging and fulfilling. It's one of the key reasons I'm applying for your {positionName} \
        position at {companyName}. Your commitment and success in {keyCompanyGoal} \
        is well known in the field and fits my passions. \
        I know from your ad that you’re seeking a {positionName} skilled in {skill1}, {skill2} and {skill3 }. \
        I think these accomplishments will put me in the picture: \
        •	{achievement1} \
        •	{achievement2} \
        •	{achievement3} \
        I'd love to speak with you soon about how my {moreSkills} can help {companyName} \
        meet its goal of {quotefromMissionStatement}. \
        Best Regards, \
        {fullName}\
        {phoneNumber}\
        {email} "

        print(seniorLevel)

    SeniorLevel()
