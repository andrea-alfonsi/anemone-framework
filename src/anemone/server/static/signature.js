(function () {

  function build([name, options]) {
    switch (options.type) {
      case 'Scalar':
        return buildScalar(name, options)
      case 'String':
        return buildString(name, options)
      default:
        return document.createTextNode("Unkown datatype" + JSON.stringify(options))
    }
  }


  ///  Build the input field for a scalar
  function buildScalar(name, options) {
    const control = document.createElement('div')
    const label = document.createElement('label')
    label.innerText = name
    const input = document.createElement('input')
    input.type = "number"
    input.defaultValue = options.default ?? 0.0
    input.min = options.min
    input.max = options.max
    input.step = options.step
    input.name = name
    input.required = options.required
    control.appendChild(label)
    control.appendChild(input)
    return control
  }

  ///  Build the input field for a string
  function buildString(name, options) {
    const control = document.createElement('div')
    const label = document.createElement('label')
    label.innerText = name
    const input = document.createElement('input')
    input.type = "text"
    input.defaultValue = options.default ?? ''
    input.name = name
    input.required = options.required
    control.appendChild(label)
    control.appendChild(input)
    return control
  }

  /// Convert ajson signature into a form
  function signatureToForm(container, signature) {
    container.innerHTML = ""
    const form = document.createElement('form')
    Object.entries(signature).map(build).forEach(control => form.appendChild(control))
    const confirmbutton = document.createElement("button")
    confirmbutton.type = "submit"
    confirmbutton.innerText = "Run"
    confirmbutton.addEventListener('click', (e) => e.preventDefault())
    form.appendChild(confirmbutton)
    container.appendChild(form)

  }

  /// Renders the signature as json in the html
  function signatureToText(container, signature) {
    const textNode = document.createTextNode(JSON.stringify(signature, null, 4))
    container.innerHTML = ""
    container.appendChild(textNode)
  }

  /// Make a fetch request to get the signature of a model/dataset/interpreter and return the result as json promise
  async function getSignature(componentType, componentId) {
    const res = await fetch('/info/' + componentType + '/' + componentId)
    return await res.json()
  }

  window.signatureToForm = signatureToForm
  window.signatureToText = signatureToText
  window.getSignature = getSignature

})()