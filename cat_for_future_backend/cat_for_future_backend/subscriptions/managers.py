from django.db.models import Manager
from django.core.exceptions import ValidationError

MAX_SUBSCRIPTION_PER_USER = 2


class SubscriptionManager(Manager):
    def create_subscription(self, user, cat):
        # Check if the user already has reached the maximum subscriptions
        current_subscriptions = self.filter(user=user).count()

        if current_subscriptions >= MAX_SUBSCRIPTION_PER_USER:
            print("DEBUG: User has reached the maximum number of subscriptions.")
            raise ValidationError(
                f"User has reached the maximum number of subscriptions ({MAX_SUBSCRIPTION_PER_USER})."
            )

        # Create a new subscription
        subscription = self.create(user=user, cat=cat)

        # Update the booking_status of the cat to True
        cat.booking_status = True
        cat.save()

        return subscription
