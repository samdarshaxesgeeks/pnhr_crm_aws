import datetime
from .models import Customer2


def create_customer(request):


   f_name = request.POST['f_name']
   l_name = request.POST['l_name']
   email = request.POST['email']
   gender = request.POST['gender']
   per_address = request.POST['per_address']
   pr_country = request.POST['pr_country']
   cor_address = request.POST['cor_address']
   cr_country = request.POST['cr_country']
   tax_id = request.POST['tax_id']
   date_of_birth = request.POST['date_of_birth']
   Age = request.POST['Age']
   high_education = request.POST['high_education']
   occupation = request.POST['occupation']
   no_of_experience = request.POST['no_of_experience']
   parent_f_name = request.POST['parent_f_name']
   parent_l_name = request.POST['parent_l_name']
   pas_no = request.POST['pas_no']
   pas_country = request.POST['pas_no']
   telephone = request.POST['telephone']
  #  indivisual = request.POST['indivisual']
  #  company = request.POST['company']
  #  company_n = request.POST['company_n']
  #  job_position = request.POST['job_position']

   contact = Contact(
     
       f_name=f_name,
       l_name=l_name,
       pr_country=pr_country,
       email=email,
       gender=gender,
       cor_address=cor_address,
       cr_country=cr_country,
       tax_id=tax_id,
       date_of_birth=date_of_birth,
       Age=Age,
       high_education=high_education,
       occupation=occupation,
       no_of_experience=no_of_experience,
       parent_f_name=parent_f_name,
       parent_l_name=parent_l_name,
       per_address=per_address,
       pas_no=pas_no,
       pas_country=pas_country,
       telephone=telephone,
        # indivisual=indivisual,
        # company_n=company_n,
        #  company=company,
        #  job_position=job_position,
    )
   contact.save()
   return contact
