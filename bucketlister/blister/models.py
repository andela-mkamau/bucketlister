from django.db import models

from .behaviours import Timestampable


class Tag(Timestampable):
    '''
    A Tag is a label to used for identification purposes
    '''
    name = models.CharField(max_length=12)

    def __repr__(self):
        return "Tag {}".format(self.name)


class Bucketlist(Timestampable):
    '''
    A Bucketlist is a collections of Items to be done by the User
    '''
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()

    # expected date to be done with this bucketlist
    due_date = models.DateTimeField()
    # whether it can be viewed bu other Users
    privacy = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name='bucketlist_tags')

    def __repr__(self):
        return "Bucketlist {}".format(self.name)


ITEM_PRIORITY = (
    ('high', 'high'),
    ('normal', 'normal'),
    ('low', 'low'),
)


class Item(Timestampable):
    '''
    An Item is a single Item  in a Bucketlist
    '''
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    done = models.BooleanField(default=False)
    priority = models.CharField(max_length=12, default='normal',
                                choices=ITEM_PRIORITY)
    bucketlist = models.ForeignKey(Bucketlist, on_delete=models.CASCADE,
                                   related_name='items')
    tags = models.ManyToManyField(Tag, related_name='item_tags')

    def __repr__(self):
        return "Item {}".format(self.name)

