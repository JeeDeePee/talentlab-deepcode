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
            class="mb-2 pointer background--white pa-2"
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
            <v-avatar size=125 class="v-avatar--responsive">
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
            'description': '<p> Daniel Fahrni:</p>"Die Aufmerksamkeit bei den Kompetenzen fokussieren."</p>' +
            ' Nach seinem Studium der Erziehungs-, Politik- und Medienwissenschaften' +
            ' in Bern und Frankfurt zog es ihn als Führungs- und Organisationsberater bald einmal ins HR. Sowohl' +
            ' als Linienverantwortlicher als auch als Experte kennt er die Herausforderungen des Management Development' +
            ' von der Pieke auf und hat diesen Bereich in grossen Organisationen aufgebaut und verantwortet.</p>2004' +
            ' gründete er die cedac AG und führt den Assessment-Spezialisten und Partner von talentlab bis heute' +
            ' erfolgreich.</p>Daniel Fahrni spricht Deutsch.'
          },
          {
            'name': 'Rahel Knecht',
            'avatar': require(`@/assets/img/people/rahel-knecht.jpg`),
            'description': '<p>Rahel Knecht:</p>"Im Zentrum steht die Stärkung der eigenen Wirksamkeit."</p>' +
            ' Rahel Knecht hat an der Universität Bern Arbeits- und Organisationspsychologie studiert und bildete' +
            ' sich in Betriebswirtschaft und Coaching weiter.</p>Sie vereint Berufspraxis als Laufbahnberaterin, Coach' +
            ' und Personalentwicklerin. Die passionierte Personalerin hat zudem umfassende Führungserfahrung als Leiterin' +
            ' Talentmanagement & Diagnostik und dann der gesamten Personalentwicklung für eine grosse Schweizerische Versicherung.' +
            ' Diese Funktion führte sie in Co-Leitung und ist somit vertraut im Umgang mit modernen Organisationsformen.</p>' +
            ' Seit 2018 amtet Rahel Knecht als Standortleiterin Bern bei unserem Partner cedac AG.</p>Rahel Knecht spricht Deutsch.'
          },
          {
            'name': 'Monika Koller Schinca',
            'avatar': require(`@/assets/img/people/monika-koller.jpg`),
            'description': '<p>Monika Koller Schinca:</p>"Durch das Lösen von Blockaden im Alltag energievoller unterwegs."</p>' +
            ' Monika Koller Schinca studierte Lebensmittelwissenschaften an der ETH in Zürich und arbeitete in Midor AG in Meilen' +
            ' in der Entwicklung von Eiswaren, bevor sie an der NLP Akademie Schweiz eine Coaching Ausbildung absolvierte. Seit 2008' +
            ' arbeitet sie als Coach und Seminarleiterin in Luzern und ist Partnerin in einer HR Consulting Boutique.</p>' +
            ' In diversen Weiterbildungen hat sie sich zur NLP Master und Trainerin, zum Wingwave Coach und zum Logosynthese Master' +
            ' und Instructor ausbilden lassen.</p>Monika Koller Schinca spricht Deutsch, Italiensich und Englisch.'
          },
          {
            'name': 'Samuel Ryser',
            'avatar': require(`@/assets/img/people/samuel-ryser.jpg`),
            'description': '<p>Monika Koller-Schinca:</p>"Bei Veränderungen und für die persönliche Entwicklung ist die Nutzung der eigenen Ressourcen und Potenziale</p>' +
            '  <p>von entscheidender Bedeutung. Nach seiner Ausbildung zum Primar- und Realschullehrer unterrichtete er und absolvierte parallel ein' +
            '  Studium der Arbeits- und Organisationspsychologie und der Sportwissenschaften an der Universität Bern, das er 2011 mit dem Master of Science in ' +
            '  Psychology abschloss.</p><p>Mit einer Zusatzausbildung in Ressourcen- und lösungsorientierter Beratung arbeitet er heute als' +
            '  Assessor und Coach bei unserem Partner cedac AG, wo er auch den  Bereich Innovation und Entwicklung verantwortet.</p><p>Samuel spricht Deutsch.</p>'
          },
        ],
        managers: [
          {
            'name': 'Daniel Fahrni',
            'avatar': require(`@/assets/img/people/daniel-fahrni.jpg`),
            'description': '<p> Daniel Fahrni:</p>"Die Aufmerksamkeit bei den Kompetenzen fokussieren."</p>' +
            ' Nach seinem Studium der Erziehungs-, Politik- und Medienwissenschaften' +
            ' in Bern und Frankfurt zog es ihn als Führungs- und Organisationsberater bald einmal ins HR. Sowohl' +
            ' als Linienverantwortlicher als auch als Experte kennt er die Herausforderungen des Management Development' +
            ' von der Pieke auf und hat diesen Bereich in grossen Organisationen aufgebaut und verantwortet.</p>2004' +
            ' gründete er die cedac AG und führt den Assessment-Spezialisten und Partner von talentlab bis heute' +
            ' erfolgreich.</p>Daniel Fahrni spricht Deutsch.'
          },
          {
            'name': 'Rahel Knecht',
            'avatar': require(`@/assets/img/people/rahel-knecht.jpg`),
            'description': '<p>Rahel Knecht:</p>"Im Zentrum steht die Stärkung der eigenen Wirksamkeit."</p>' +
            ' Rahel Knecht hat an der Universität Bern Arbeits- und Organisationspsychologie studiert und bildete' +
            ' sich in Betriebswirtschaft und Coaching weiter.</p>Sie vereint Berufspraxis als Laufbahnberaterin, Coach' +
            ' und Personalentwicklerin. Die passionierte Personalerin hat zudem umfassende Führungserfahrung als Leiterin' +
            ' Talentmanagement & Diagnostik und dann der gesamten Personalentwicklung für eine grosse Schweizerische Versicherung.' +
            ' Diese Funktion führte sie in Co-Leitung und ist somit vertraut im Umgang mit modernen Organisationsformen.</p>' +
            ' Seit 2018 amtet Rahel Knecht als Standortleiterin Bern bei unserem Partner cedac AG.</p>Rahel Knecht spricht Deutsch.'
          },
          {
            'name': 'Lis Spühler Schaffroth',
            'avatar': require(`@/assets/img/people/lis-spuehler.jpg`),
            'description': '<p>Lis Spühler Schaffroth:</p>"Gewinnen Sie an Souveränität!"</p>' +
            ' Lis Spühler Schaffroth ist Psychologin mit langjähriger Führungs-, Beratungs- und Coachingerfahrung.' +
            ' Sie hat Weiterbildungen unter anderem in Konfliktmanagement, Mediation und strategischem Management absolviert.' +
            ' Direkte Anwendbarkeit im Berufsalltag und die Stärkung des Selbst stehen dabei im Zentrum. Gemeinsam werden spezifische Lösungsansätze' +
            ' zur Erweiterung der persönlichen Handlungsoptionen entwickelt.</p>' +
            ' Lis Spühler Schaffroth arbeitet selbständig im Bereich Personal- und Organisationsentwicklung sowie psychologische Beratung.</p>' +
            ' Lis Spühler Schaffroth spricht Deutsch und Französisch.'
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
