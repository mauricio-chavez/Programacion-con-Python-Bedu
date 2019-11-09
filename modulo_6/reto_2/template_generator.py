from html import start

def bedu_travels_template(productos):
    html = start
    total = 0

    for producto in productos:
        total += float(producto[3])
        html += """
            <tr>
              <td>{}</td>
              <td>${}</td>
              <td>{}</td>
              <td>${}</td>
            </tr>
        """.format(producto[0], producto[1], producto[2], producto[3])

    html += """
          <tr>
            <td>&nbsp;</td>
            <td>&nbsp;</td>
            <td>Total</td>
            <td>${}</td>
          </tr>
        </tbody>
      </table>
    <p>&nbsp;</p>
    """.format(total)

    return html
    
    
