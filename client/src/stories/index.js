import {storiesOf} from '@storybook/vue';
// import custom components
import Tools from '../components/module/Tools.vue';
import Unit from '../components/module/Unit.vue';
import MyButton from './Button.vue';

storiesOf('Module', module)
  .add('tools', () => ({
    components: {Tools},
    template: '<Tools :tools="tools"></Tools>',
    data() {
      return {
        tools: [
          {
            type: 'link',
            value: {
              url: 'https://talentlab-web.s3.amazonaws.com/documents/dummy_clxGRR6.pdf',
              document: 'https://talentlab-web.s3.amazonaws.com/documents/dummy_clxGRR6.pdf',
              description: 'Rem temporibus'
            }
          },
          {
            type: 'link',
            value: {
              url: 'https://talentlab-web.s3.amazonaws.com/documents/dummy_clxGRR6.pdf',
              document: 'https://talentlab-web.s3.amazonaws.com/documents/dummy_clxGRR6.pdf',
              description: 'Rem temporibus'
            }
          }
        ]
      }
    }
  }))
  .add('unit', () => ({
    components: {Unit},
    template: '<Unit :unit="unit" :booked="booked"></Unit>',
    data() {
      return {
        booked: true,
        unit: {
          title: 'Partnering Modelle',
          teaser: 'Unternehmensübergreifende Zusammenarbeit kann entlang von …',
          type: 'Webinar',
          count: '8 Lektionen',
          duration: '4 Stunden'
        }
      }
    }
  }));

storiesOf('Button', module)
  .add('button template', () => ({
    template: '<my-button :rounded="true">round</my-button>'
  }))
  .add('rounded button', () => ({
    components: {MyButton},
    template: '<my-button :rounded="true">rounded</my-button>'
  }))
  .add('normal button', () => ({
    components: {MyButton},
    template: '<my-button :rounded="false">normal</my-button>'
  }));
