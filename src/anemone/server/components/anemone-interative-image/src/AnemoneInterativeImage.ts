import { html, css, LitElement, BooleanAttributePart } from 'lit';
import { property, query } from 'lit/decorators.js';

enum CursorState {
  DRAW,
  DRAG
}

export class AnemoneInterativeImage extends LitElement {
  static styles = css`
    :host {
      display: block;
      color: var(--anemone-interative-image-text-color, #000);
    }

    .draggable {
      fill: var(--region-background-color, rgba(0,120,215,0.3));
      stroke: var(--region-border-color, #0078D7 );
    }
  `;

  @query('#mainSVG') mainSVG?: SVGSVGElement;
  @query('#image') image?: SVGImageElement;

  @property({ type: Boolean }) regionSelector = false;
  @property({ type: String }) src?: string;
  @property({ type: Number }) width?: number;
  @property({ type: Number }) height?: number;

  mode?: CursorState;
  startX?: number;
  startY?: number;
  regionSelectorRect?: SVGRectElement;
  dragX?: number
  dragY?: number
  origX?: number
  origY?: number

  render() {
    this.addEventListener("mousedown", this._handleMouseDown);
    return html`
      <svg width="${this.width}" height="${this.height}" xmlns="http://www.w3.org/2000/svg" id="mainSVG">
        <image x="0" y="0" width="${this.width}" height="${this.height}" href="${this.src}" id="image" crossOrigin="Anonymous" />
      </svg>
    `;
  }

  _handleMouseDown(e: MouseEvent) {
    //@ts-ignore
    if (e.composedPath()[0].tagName === 'image') {
      if (this.regionSelectorRect) {
        this.regionSelectorRect.remove()
      }
      this.mode = CursorState.DRAW;
      this.startX = e.offsetX;
      this.startY = e.offsetY;
      this.regionSelectorRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
      this.regionSelectorRect.setAttribute('x', '' + this.startX);
      this.regionSelectorRect.setAttribute('y', '' + this.startY);
      this.regionSelectorRect.setAttribute('width', '0');
      this.regionSelectorRect.setAttribute('height', '0');
      this.regionSelectorRect.classList.add('draggable');
      this.mainSVG?.appendChild(this.regionSelectorRect);
      //@ts-ignore
    } else if (e.composedPath()[0].tagName === 'rect') {
      this.mode = CursorState.DRAG;
      this.dragX = e.clientX;
      this.dragY = e.clientY;
      this.origX = parseFloat(this.regionSelectorRect?.getAttribute('x') ?? '0');
      this.origY = parseFloat(this.regionSelectorRect?.getAttribute('y') ?? '0');
    }

    if (this.mode) {
      this.addEventListener('mousemove', this._handleMouseMove);
      this.addEventListener('mouseup', this._handleMouseUp);
      this.addEventListener('mouseleave', this._handleMouseUp);
    }
  }

  _handleMouseMove(e: MouseEvent) {
    if (this.mode === CursorState.DRAW) {
      const w = e.offsetX - (this.startX ?? 0);
      const h = e.offsetY - (this.startY ?? 0);
      this.regionSelectorRect?.setAttribute('width', '' + Math.abs(w));
      this.regionSelectorRect?.setAttribute('height', '' + Math.abs(h));
      this.regionSelectorRect?.setAttribute('x', '' + (w < 0 ? e.offsetX : this.startX ?? 0));
      this.regionSelectorRect?.setAttribute('y', '' + (h < 0 ? e.offsetY : this.startY ?? 0));
    } else if (this.mode === CursorState.DRAG) {
      const dx = e.clientX - (this.dragX ?? 0);
      const dy = e.clientY - (this.dragY ?? 0);
      this.regionSelectorRect?.setAttribute('x', '' + ((this.origX ?? 0) + dx));
      this.regionSelectorRect?.setAttribute('y', '' + ((this.origY ?? 0) + dy));
    }
  }

  _handleMouseUp() {
    this.removeEventListener('mousemove', this._handleMouseMove);
    this.removeEventListener('mouseup', this._handleMouseUp);
    this.mode = undefined;

    if (!this.regionSelectorRect) {
      return;
    }

    const x = +(this.regionSelectorRect?.getAttribute('x') ?? 0);
    const y = +(this.regionSelectorRect?.getAttribute('y') ?? 0);
    const w = +(this.regionSelectorRect?.getAttribute('width') ?? 0);
    const h = +(this.regionSelectorRect?.getAttribute('height') ?? 0);

    let offsetCanvas = document.createElement('canvas');
    offsetCanvas.width = w;
    offsetCanvas.height = h;
    // @ts-ignore
    offsetCanvas.getContext('2d')?.drawImage(this.image, x, y, w, h, 0, 0, w, h);
    const data = offsetCanvas.toDataURL();
    const detail = {
      data: data
    };

    const ev = new CustomEvent('selectedRegionChange', {
      detail,
      bubbles: true,
      cancelable: false
    });
    this.dispatchEvent(ev);
  }
}
