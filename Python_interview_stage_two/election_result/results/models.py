from django.db import models

# Create your models here.
class AgentName(models.Model):
    name_id = models.AutoField(primary_key=True, null=False)
    firstname = models.CharField(max_length=255, null=False)
    lastname = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, default=None)
    phone = models.CharField(max_length=13, null=False)
    pollingunit_uniqueid = models.IntegerField(null=False)

    # class Meta:
    #     db_table = 'agentname'
    #     options = {
    #         'engine': 'MyISAM',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.firstname

class AnnouncedLgaResults(models.Model):
    result_id = models.AutoField(primary_key=True, null=False)
    lga_name = models.CharField(max_length=255, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.TextField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'announced_lga_results'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.party_abbreviation


class AnnouncedPuResults(models.Model):
    result_id = models.AutoField(primary_key=True, null=False)
    polling_unit_uniqueid = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.TextField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'announced_pu_results'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.party_abbreviation


class AnnouncedStateResults(models.Model):
    result_id = models.AutoField(primary_key=True, null=False)
    state_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.TextField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'announced_state_results'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.state_name


class AnnouncedWardResults(models.Model):
    result_id = models.AutoField(primary_key=True, null=False)
    ward_name = models.CharField(max_length=50, null=False)
    party_abbreviation = models.CharField(max_length=4, null=False)
    party_score = models.IntegerField(null=False)
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.TextField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'announced_ward_results'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.ward_name


class Lga(models.Model):
    uniqueid = models.AutoField(primary_key=True, null=False)
    lga_id = models.IntegerField(null=False)
    lga_name = models.CharField(max_length=50, null=False)
    state_id = models.IntegerField(null=False)
    lga_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.TextField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'lga'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.lga_name


class Party(models.Model):
    partyid = models.CharField(max_length=11, null=False)
    partyname = models.CharField(max_length=11, null=False)

    # class Meta:
    #     db_table = 'party'
    #     options = {
    #         'engine': 'MyISAM',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.partyname


class PollingUnit(models.Model):
    uniqueid = models.AutoField(primary_key=True, null=False)
    polling_unit_id = models.IntegerField(null=False)
    ward_id = models.IntegerField(null=False)
    lga_id = models.IntegerField(null=False)
    uniquewardid = models.IntegerField(default=None)
    polling_unit_number = models.CharField(max_length=50, null=True)
    polling_unit_name = models.CharField(max_length=50, null=True)
    polling_unit_description = models.TextField(null=True)
    lat = models.CharField(max_length=255, null=True)
    long = models.CharField(max_length=255, null=True)
    entered_by_user = models.CharField(max_length=50, null=True)
    date_entered = models.TextField(null=True)
    user_ip_address = models.CharField(max_length=50, null=True)

    # class Meta:
    #     db_table = 'polling_unit'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.polling_unit_name


class States(models.Model):
    state_id = models.AutoField(primary_key=True, null=False)
    state_name = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'states'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.state_name


class Ward(models.Model):
    uniqueid = models.AutoField(primary_key=True, null=False)
    ward_id = models.IntegerField(null=False)
    ward_name = models.CharField(max_length=50, null=False)
    lga_id = models.IntegerField(null=False)
    ward_description = models.TextField()
    entered_by_user = models.CharField(max_length=50, null=False)
    date_entered = models.TextField(null=False)
    user_ip_address = models.CharField(max_length=50, null=False)

    # class Meta:
    #     db_table = 'ward'
    #     options = {
    #         'engine': 'InnoDB',
    #         'charset': 'latin1',
    #     }

    def __str__(self):
        return self.ward_name