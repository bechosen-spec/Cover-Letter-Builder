# This is the Class for entry level of the cover-letter builder
class EntryLvl:
    def EntryLevel():
        jobTitle = input("Job Title: ")
        organizationName = input("Organization Name: ")
        skill1 = input("Skill  No. 1: ")
        skill2 = input("Skill  No. 2: ")
        skill3 = input("Skill  No. 3: ")
        careerField = input("Career Field: ")
        motivation = input("Something That Motivates You to Join In: ")
        achievement1 = input(
            "Achievement  No. 1 that Used a Skill they Need: ")
        achievement2 = input(
            "Achievement  No. 2 that Used a Skill they Need: ")
        achievement3 = input(
            "Achievement  No. 3 that Used a Skill they Need: ")
        skillsTheyNeed = input("Two Skills They Need: ")
        fullName = input("Full Name: ")
        phoneNumber = input("Phone Number: ")
        email = input("Email: ")

        coverLetter = f"I'm excited to apply for the {jobTitle} position at{organizationName}. Although\
    I'm an entry-level applicant, I am passionate about doing a great job and out of the skills you're looking for \
    I have already developed {skill1}, {skill2}, {skill3}.\
    I'm very interested in beginning a career in the {careerField} field, as I {motivation}.\
    believe I'll make an excellent {jobTitle} thanks to my skills, plus the following accomplishments: \
    {achievement1} \
    {achievement2} \
    {achievement3} \
    I'm excited to show you how my {skillsTheyNeed} can help you achieve your \
    upcoming goals. Could we set up a time to discuss your needs? \
    Best Regards, \
    {fullName}  \
    {phoneNumber}  \
    {email} \"                                                                                                                                                                                                                                                "
        print(coverLetter)

    EntryLevel()
