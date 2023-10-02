from django import forms
from django.core.exceptions import ValidationError

class BlogPostForm(forms.Form):
    
    category = forms.ChoiceField(choices=(
        ('Select Category', 'Select Category'),
        ('hotels', 'Hotels'),
        ('travel', 'Travel'),
        ('lifestyle', 'Lifestyle'),
        ('airline', 'Airline'),
    ), widget=forms.Select(attrs={'class': 'outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'category', 'placeholder': 'Add Category'}))

    title = forms.CharField(label='Title', max_length=100, widget=forms.TextInput(attrs={
                            'class': 'inptitle outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'heading', 'placeholder': 'Add Title'}))
    location = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'id': 'location-input', 'class': 'inploc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'location', 'placeholder': 'Add Location'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpcontent outline-none border-none form-control w-75  mx-auto mt-4 border-bottom Responsive_text_for_Blog_Details', 'name': 'content', 'placeholder': 'Add Content'}))
    thumbnail = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'thumbnail', 'placeholder': 'Add Thumbnail','onchange':"validateFileSize(this)"}))

    # first subform (all fields are required)
    subheading1 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading1', 'placeholder': 'Add Sub Heading'}))
    subloc1 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc1', 'placeholder': 'Add Sub Location'}),required=False)
    subimage1 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage1', 'placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}))
    subtext1 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext1', 'placeholder': 'Add Sub Text'}))

    # second subform
    subheading2 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading2', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc2 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc2', 'placeholder': 'Add Sub Location'}), required=False)
    subimage2 = forms.ImageField( widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage2','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext2 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext2','placeholder': 'Add Sub Text'}), required=False)

    # third subform
    subheading3 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading3', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc3 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc3', 'placeholder': 'Add Sub Location'}), required=False)
    subimage3 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage3','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext3 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext3','placeholder': 'Add Sub Text'}), required=False)

    # fourth subform
    subheading4 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading4', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc4 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc4', 'placeholder': 'Add Sub Location'}), required=False)
    subimage4 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage4','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext4 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext4','placeholder': 'Add Sub Text'}), required=False)

    # fifth subform
    subheading5 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading5', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc5 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc5', 'placeholder': 'Add Sub Location'}), required=False)
    subimage5 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage5','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext5 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext5','placeholder': 'Add Sub Text'}), required=False)

    # sixth subform
    subheading6 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading6', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc6 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc6', 'placeholder': 'Add Sub Location'}), required=False)
    subimage6 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage6','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext6 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext6','placeholder': 'Add Sub Text' }), required=False)

    # seventh subform
    subheading7 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading7', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc7 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc7', 'placeholder': 'Add Sub Location'}), required=False)
    subimage7 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage7','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext7 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext7','placeholder': 'Add Sub Text'}), required=False)

    # eighth subform
    subheading8 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading8', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc8 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc8', 'placeholder': 'Add Sub Location'}), required=False)
    subimage8 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage8','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext8 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext8','placeholder': 'Add Sub Text'}), required=False)

    # ninth subform
    subheading9 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading9', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc9 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc9', 'placeholder': 'Add Sub Location'}), required=False)
    subimage9 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage9','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext9 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext9','placeholder': 'Add Sub Text'}), required=False)

    # tenth subform
    subheading10 = forms.CharField(label='Heading', max_length=100, widget=forms.TextInput(
        attrs={'class': 'inpsubheading outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subheading10', 'placeholder': 'Add Sub Heading'}), required=False)
    subloc10 = forms.CharField(label='Location', max_length=50, widget=forms.TextInput(
        attrs={'class': 'inpsubloc outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subloc10', 'placeholder': 'Add Sub Location'}), required=False)
    subimage10 = forms.ImageField(widget=forms.ClearableFileInput(
        attrs={'class': 'rounded image outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subimage10','placeholder': 'Add Sub Image','onchange':"validateFileSize(this)"}), required=False)
    subtext10 = forms.CharField(label='Content', widget=forms.Textarea(
        attrs={'class': 'inpsubtext Responsive_text_for_Blog_Details outline-none border-none form-control w-75  mx-auto mt-4 border-bottom', 'name': 'subtext10','placeholder': 'Add Sub Text'}), required=False)



class CommentForm(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control col-lg-12 col-md-12 col-sm-12 col-12',
            'placeholder': 'Add Comments',
            'rows': 1,
            'cols': 50
        }))


class AdminCommentForm(forms.Form):
    CHOICES = [
        ('Approve', 'Approve'),
        ('Reject', 'Reject'),
    ]
    status = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    content = forms.CharField(label="", required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 4,
            'cols': 50,
        }))


class ReplyForm(forms.Form):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'reply!',
            'rows': 2,
            'cols': 50
        }))


class ReportForm(forms.Form):
    REPORT_CHOICES = (
        ('Select Options', 'Select Options'),
        ('harassment', 'Harassment'),
        ('bullying', 'Bullying'),
        ('harmful', 'Harmful Content'),
        ('sexual', 'Sexual Content'),
        ('child_abuse', 'Child Abuse'),
        ('spam', 'Spam'),
    )

    report_type = forms.ChoiceField(
        choices=REPORT_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    reason = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control'}))