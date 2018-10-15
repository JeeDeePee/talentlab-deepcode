<template>
  <div>

    <h1 class="text--violet text-xs-center">Mit wem möchtest Du arbeiten?</h1>
    <div class="lead my-3 text-xs-center">Finde Deinen Coach. Folgende Coaches haben Erfahrung mit den gewählten
      Themen:
    </div>

    <div class="small--content">
      <v-layout row wrap>
        <v-flex xs12 sm6>
          <h3 class="my-3 text--violet">Professionelle Coaches</h3>
          <div class="mb-2 pointer background--white pa-2"
               v-for="(item,i) in coaches" :key="i"
               @click="select(item)"
          >
            <v-avatar size=50 class="v-avatar--responsive">
              <v-img
                :src="item.avatar"
                :alt="item.name"
              ></v-img>
            </v-avatar>
            <span class="ml-2">
          {{item.name}}
          </span>
          </div>
        </v-flex>
        <v-flex xs12 sm6>
          <h3 class="my-3 text--violet">Erfahrene Manager</h3>
          <div
            class="mb-3 pointer background--white pa-2"
            v-for="(item,i) in managers" :key="i"
            @click="select(item)"
          >
            <v-avatar size=50 class="v-avatar--responsive">
              <v-img
                :src="item.avatar"
                :alt="item.name"
              ></v-img>
            </v-avatar>
            <span class="ml-2">
          {{item.name}}
          </span>
          </div>
        </v-flex>
      </v-layout>

      <div v-if="selected" class="background--beige mt-3 pa-4">
        <v-layout>
          <v-flex xs4>
            <v-avatar size=100 class="v-avatar--responsive">
              <v-img
                :src="selected.avatar"
                :alt="selected.name"
              ></v-img>
            </v-avatar>
            <h3 class="mt-2">
              {{selected.name}}
            </h3>
          </v-flex>

          <v-flex xs8>
            <div v-html="selected.description">
            </div>
          </v-flex>

        </v-layout>
      </div>
    </div>

    <div class="mt-5 text-xs-center">
      <v-btn class="btn-secondary mr-2" @click="$emit('back', 'Topics')">Zurück</v-btn>
      <v-btn @click="save" class="ml-2">Coach auswählen</v-btn>
    </div>
  </div>
</template>

<script>

  export default {
    components: {},
    data() {
      return {
        checked: [],
        selected: null,
        coaches: [
          {
            'name': 'Peter Naumann',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Peter Naumann',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Felix Muster',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          }
        ],
        managers: [
          {
            'name': 'Max Muster',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Peter Frei',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          },
          {
            'name': 'Nico Gebrer',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p><p>Er arbeitet als Assessor und Coach bei unserem Partner cedac AG, wo er auch den Bereich Innovation und Entwicklung verantwortet.\n' +
            '              Sprachen: Deutsch.</p>'
          }
        ]
      }
    },
    methods: {
      select(item) {
        this.selected = item
      },
      save() {
        this.$emit('proceed', 'Organize')
      }
    }
  }
</script>
