import {storiesOf} from '@storybook/vue';
// import custom components
import Tools from '../components/module/Tools.vue';
import Unit from '../components/module/Unit.vue';

storiesOf('TestUnit', module)
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
        unit: {title: 'Title', teaser: 'Teaser', type: 'Type', count: '3 Durchführungen', duration: '1 1/2 Stunden'}
      }
    }
  }));
