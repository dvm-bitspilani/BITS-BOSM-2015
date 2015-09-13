from registration.models import UserProfile
from django.contrib.auth.models import User
from nocaptcha_recaptcha.fields import NoReCaptchaField
from django import forms

cities= (
    ('Alwar','Alwar'),
    ('Bahadurgarh','Bahadurgarh'),
    ('Bangalore','Bangalore'),
    ('Bareilly','Bareilly'),
    ('Bellary','Bellary'),
    ('Berhampur','Berhampur'),
    ('Bahadurgarh','Bahadurgarh'),
    ('Bhilai','Bhilai'),
    ('Bhiwani','Bhiwani'),
    ('Bhopal','Bhopal'),
    ('Bhubaneswar','Bhubaneswar'),
    ('Bikaner','Bikaner'),
    ('Bilaspur','Bilaspur'),
    ('Chandigarh','Chandigarh'),
    ('Chennai','Chennai'),
    ('Chirawa','Chirawa'),
    ('Chitoor','Chitoor'),
    ('Chittorgarh','Chittorgarh'),
    ('Cochin','Cochin'),
    ('Coimbatore','Coimbatore'),
    ('Dehradun','Dehradun'),
    ('Deogarh','Deogarh'),
    ('Dindigul','Dindigul'),
    ('Faridabad','Faridabad'),
    ('Faridkot','Faridkot'),
    ('Gandhinagar','Gandhinagar'),
    ('Ghaziabad','Ghaziabad'),
    ('Goa','Goa'),
    ('Guna','Guna'),
    ('Guntur','Guntur'),
    ('Gurgaon','Gurgaon'),
    ('Gwalior','Gwalior'),
    ('Hamirpur','Hamirpur'),
    ('Hissar','Hissar'),
    ('Hyderabad','Hyderabad'),
    ('Indore','Indore'),
    ('Jaipur','Jaipur'),
    ('Jammu','Jammu'),
    ('Jhajjar','Jhajjar'),
    ('Jhalawar','Jhalawar'),
    ('Jhansi','Jhansi'),
    ('Jhunjhunu','Jhunjhunu'),
    ('Jodhpur','Jodhpur'),
    ('Kannur','Kannur'),
    ('Kanpur','Kanpur'),
    ('Kharagpur','Kharagpur'),
    ('Kolkata','Kolkata'),
    ('Kota','Kota'),
    ('Kurukshetra','Kurukshetra'),
    ('Lakshmangarh','Lakshmangarh'),
    ('Latur','Latur'),
    ('Lucknow','Lucknow'),
    ('Madurai','Madurai'),
    ('Mandi','Mandi'),
    ('Mathura','Mathura'),
    ('Meerut','Meerut'),
    ('Mohali','Mohali'),
    ('Moradabad','Moradabad'),
    ('Mumbai','Mumbai'),
    ('Nagpur','Nagpur'),
    ('Narasaraopet','Narasaraopet'),
    ('Nashik','Nashik'),
    ('Neemrana','Neemrana'),
    ('Nellore','Nellore'),
    ('New Delhi','New Delhi'),
    ('Noida','Noida'),
    ('Panipat','Panipat'),
    ('Patiala','Patiala'),
    ('Patna','Patna'),
    ('Pilani','Pilani'),
    ('Pondicherry','Pondicherry'),
    ('Pune','Pune'),
    ('Rohtak','Rohtak'),
    ('Roorkee','Roorkee'),
    ('Rupnagar','Rupnagar'),
    ('Sadopur','Sadopur'),
    ('Saharanpur','Saharanpur'),
    ('Salem','Salem'),
    ('Sambalpur','Sambalpur'),
    ('Sangur','Sangur'),
    ('Sarang','Sarang'),
    ('Shimla','Shimla'),
    ('Sikar','Sikar'),
    ('Sonepat','Sonepat'),
    ('Srikakulam','Srikakulam'),
    ('Srinagar','Srinagar'),
    ('Surathkal','Surathkal'),
    ('Tiruchengode','Tiruchengode'),
    ('Thiruvananthapuram','Thiruvananthapuram'),
    ('Udaipur','Udaipur'),
    ('Ujjain','Ujjain'),
    ('Vadodara','Vadodara'),
    ('Varanasi','Varanasi'),
    ('Vellore','Vellore'),
    ('Vijayawada','Vijayawada'),
    ('Vilani','Vilani'),
    ('Villupuram','Villupuram'),
    ('Vishakapatnam','Vishakapatnam'),
    ('Vizag','Vizag'),
    ('Warangal','Warangal'),
    ('Other','Other'),
    )

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(), 
        }

class UserProfileForm(forms.ModelForm):
    phone = forms.RegexField(regex=r'^\d{10}$', error_message = ("Enter a valid 10 digit mobile number!"))
    captcha = NoReCaptchaField()
    class Meta:
        model = UserProfile
        fields = ('firstname', 'lastname', 'college','city','phone')
        widgets = {
            'city': forms.Select(choices=cities),
        }