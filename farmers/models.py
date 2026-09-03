from django.db import models

SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
STATUS_CHOICES = [('active', 'Active'), ('inactive', 'Inactive')]
LOAN_STATUS_CHOICES = [('ongoing', 'Ongoing'), ('completed', 'Completed'), ('defaulted', 'Defaulted')]

class Farmer(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    address = models.TextField()
    municipality = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    date_added = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    guarantor = models.CharField(max_length=200)
    guarantor_contact = models.CharField(max_length=20)
    approver = models.CharField(max_length=200)

    def __str__(self):
        return self.last_name + ', ' + self.first_name


class FarmerLoan(models.Model):
    date_released = models.DateField()
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='loans')
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    total_value = models.DecimalField(max_digits=12, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=LOAN_STATUS_CHOICES, default='ongoing')
    fertilizer_type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.total_value = self.quantity * self.unit_cost
        super().save(*args, **kwargs)

class Payment(models.Model):
    loan = models.ForeignKey(FarmerLoan, on_delete=models.CASCADE, related_name='payments')
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name='payments')
    date_paid = models.DateField(auto_now_add=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    collected_by = models.CharField(max_length=200)
    remarks = models.TextField(blank=True)




