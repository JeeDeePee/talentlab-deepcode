import graphene
from graphene import InputObjectType, relay

from focus.schema.schema import CompetenceEntryNode


# class CompetenceEntryInput(InputObjectType):
#     focus_id = graphene.Int(required=True)
#     competence_slug = graphene.String(required=True)
#     current_level = graphene.Int(required=True)
#     next_evaluation = graphene.Date(required=False)


class CreateCompetenceEntry(relay.ClientIDMutation):
    class Input:
        focus_id = graphene.Int(required=True)
        competence_slug = graphene.String(required=True)
        current_level = graphene.Int(required=True)
        next_evaluation = graphene.Date(required=False)
        # input = graphene.Argument(CompetenceEntryInput)

    new_competence_node = graphene.Field(CompetenceEntryNode)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):

        print('called CreateCompetenceEntry mutation')

        entry_data = args.get('competence_entry_input')
        # new_competence_node  = CompetenceEntry()
        new_competence_node = None

        return cls(new_competence_node=new_competence_node)


class UpdateCompetenceEntry(relay.ClientIDMutation):
    class Input:
        focus_id = graphene.Int(required=True)
        competence_slug = graphene.String(required=True)
        current_level = graphene.Int(required=True)
        next_evaluation = graphene.Date(required=False)
        # input = graphene.Argument(CompetenceEntryInput)
        # id = graphene.String(required=True)

    errors = graphene.List(graphene.String)
    updated_competence_entry = graphene.Field(CompetenceEntryNode)

    @classmethod
    def mutate_and_get_payload(cls, args, context, info):

        print('called UpdateCompetenceEntry mutation')

        return cls(updated_competence_entry=None)

        # try:
        #     book_instance = get_object(Book, args['id']) # get book by id
        #     if book_instance:
        #         # modify and update book model instance
        #         book_data = args.get('book')
        #         updated_book = update_create_instance(book_instance, book_data)
        #         return cls(updated_book=updated_book)
        # except ValidationError as e:
        #     # return an error if something wrong happens
        #     return cls(updated_book=None, errors=get_errors(e))


class FocusMutation(object):
    create_competence_entry = CreateCompetenceEntry.Field()
    update_competence_entry = UpdateCompetenceEntry.Field()
