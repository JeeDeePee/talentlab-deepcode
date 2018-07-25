import graphene
from graphene import InputObjectType, relay

from focus.models import CompetenceEntry, Focus, Competence
from focus.schema.schema import FocusNode


class CompetenceEntryInput(InputObjectType):
    slug = graphene.String(required=True)
    current_level = graphene.Int(required=True)
    next_evaluation = graphene.Date(required=False)


class FocusInput(InputObjectType):
    entries = graphene.List(CompetenceEntryInput)


class CreateFocus(relay.ClientIDMutation):
    class Input:
        input = graphene.Argument(FocusInput)

    new_focus_node = graphene.Field(FocusNode)
    # feedback = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        user = info.context.user
        params = input.get('input')

        # disable old focus
        all_user_focus = Focus.objects.filter(user=user)
        for user_focus in all_user_focus:
            user_focus.active = False
            user_focus.save()

        # create new focus
        focus = Focus(user=user, active=True)
        focus.save()

        # create competence entries for this focus
        for ce_input in params.entries:
            competence = Competence.objects.get(slug=ce_input.slug)
            competence_entry = CompetenceEntry(focus=focus,
                                               competence=competence,
                                               current_level=ce_input.current_level,
                                               next_evaluation=ce_input.next_evaluation)
            competence_entry.save()

        # focus_node = FocusNode()
        # return cls(feedback="OK")
        new_focus_node = FocusNode(focus)
        return cls(new_focus_node=new_focus_node)


class FocusMutation(object):
    create_focus = CreateFocus.Field()
