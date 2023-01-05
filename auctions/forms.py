from django.forms import ModelForm, TextInput
from auctions.models import Listing, Bid



class NewListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['owner_id', 'winner_id', 'is_active']
        widgets = {            
            'title': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px;',
                
                }),
             'description': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px; height : 300px;', 
              
                }),
            'image': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Must be URL for PNG/JPG/JPEG File (optional)'
                }),
            
        }

class NewBidForm(ModelForm):
    class Meta:
        model = Bid
        fields = '__all__'
        exclude = ['user_id', 'listing_id', 'Timestamp']
   
