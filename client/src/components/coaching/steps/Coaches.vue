<template>
  <div>

    <h1 class="text--violet text-xs-center">Mit welchem Coach möchtest Du arbeiten?</h1>
    <div class="lead my-3 text-xs-center">Folgende Coaches haben Erfahrung mit den gewählten
      Themen:
    </div>

    <div class="small--content">
      <v-layout row wrap>
        <v-flex xs12 sm6>
          <h3 class="my-3 text--violet">Ausgebildete Coaches</h3>
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
      <v-btn @click="save" class="ml-2">weiter</v-btn>
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
            'name': 'Daniel Fahrni',
            'avatar': require(`@/assets/img/people/daniel-fahrni.jpg`),
            'description': '<p> Daniel Fahrni legt als Coach Wert darauf, die Aufmerksamkeit bei den.' +
            ' Kompetenzen zu fokussieren.</p>Nach seinem Studium der Erziehungs-, Politik- und Medienwissenschaften' +
            ' in Bern und Frankfurt zog es ihn als Führungs- und Organisationsberater bald einmal ins HR. Sowohl' +
            ' als Linienverantwortlicher als auch als Experte kennt er die Herausforderungen des Management Development' +
            ' von der Pieke auf und hat diesen Bereich in grossen Organisationen aufgebaut und verantwortet.</p>2004' +
            ' gründete er die cedac AG und führt den Assessment-Spezialisten und Partner von talentlab bis heute' +
            ' erfolgreich.</p>Daniel Fahrni spricht Deutsch.'
          },
          {
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Samuel Ryser ist ein erfahrener Coach bei der Begleitung von  Teamentwicklungsprozessen.</p>' +
            '  <p>Nach seiner Ausbildung zum Primar- und Realschullehrer unterrichtete er und absolvierte parallel ein Studium der Arbeits-' +
            '  und Organisationspsychologie und der Sportwissenschaften an der Universität Bern, das er 2011 mit dem Master of Science in ' +
            '  Psychology abschloss.</p><p>Heute arbeitet er als Assessor und Coach bei unserem Partner cedac AG, wo er auch den  Bereich ' +
            '  Innovation und Entwicklung verantwortet.</p><p>Samuel spricht bei der Arbeit (Bern-)Deutsch.</p>'
          },
        ],
        managers: [
          {
            'name': 'Daniel Fahrni',
            'avatar': require(`@/assets/img/people/daniel-fahrni.jpg`),
            'description': '<p> Daniel Fahrni legt als Coach Wert darauf, die Aufmerksamkeit die Aufmerksamkeit bei den.' +
            ' Kompetenzen zu fokussieren.</p>Nach seinem Studium der Erziehungs-, Politik- und Medienwissenschaften' +
            ' in Bern und Frankfurt zog es ihn als Führungs- und Organisationsberater bald einmal ins HR. Sowohl' +
            ' als Linienverantwortlicher als auch als Experte kennt die Herausforderungen des Management Development' +
            ' von der Pieke auf und hat diesen Bereich in grossen Organisationen aufgebaut und verantwortet.</p>2004' +
            ' gründete er die cedac AG und führt den Assessment-Spezialisten und Partner von talentlab bis heute' +
            ' erfolgreich.</p>Daniel Fahrni spricht Deutsch.'
          },
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
