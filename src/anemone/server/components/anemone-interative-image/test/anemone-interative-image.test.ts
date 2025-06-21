import { html } from 'lit';
import { fixture, expect } from '@open-wc/testing';
import { AnemoneInterativeImage } from '../src/AnemoneInterativeImage.js';
import '../src/anemone-interative-image.js';

describe('AnemoneInterativeImage', () => {
  // it('has a default header "Hey there" and counter 5', async () => {
  //   const el = await fixture<AnemoneInterativeImage>(html`<anemone-interative-image></anemone-interative-image>`);

  //   expect(el.header).to.equal('Hey there');
  //   expect(el.counter).to.equal(5);
  // });

  // it('increases the counter on button click', async () => {
  //   const el = await fixture<AnemoneInterativeImage>(html`<anemone-interative-image></anemone-interative-image>`);
  //   el.shadowRoot!.querySelector('button')!.click();

  //   expect(el.counter).to.equal(6);
  // });

  // it('can override the header via attribute', async () => {
  //   const el = await fixture<AnemoneInterativeImage>(html`<anemone-interative-image header="attribute header"></anemone-interative-image>`);

  //   expect(el.header).to.equal('attribute header');
  // });

  // it('passes the a11y audit', async () => {
  //   const el = await fixture<AnemoneInterativeImage>(html`<anemone-interative-image></anemone-interative-image>`);

  //   await expect(el).shadowDom.to.be.accessible();
  // });
});
