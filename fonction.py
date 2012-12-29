# -*-coding:Utf-8 -*

class Fonction:
    """ Cette classe regroupe les commentaires d'une fonction en un
    objet.
    m_nom
    m_description
    m_args : tableau associatif 'registre : description'
    """

    def __init__(self, nom, description, args):
        """ args est un tableau associatif """
        self.m_nom = nom
        self.m_description = description
        self.m_args = args

    def getHTML(self):
        """ Retourne un string en HTML de l'objet """
        html = "<section>"
        html += "<h1>" + self.m_nom + "</h1>"
        html += "<p>" + self.m_description + "</p>"
        html += "<dl>"
        for key in self.m_args:
            html += "<dt>" + key + "</dt>"
            html += "<dd>" + self.m_args[key] + "</dd>"
        html += "</dl>"
        html += "</section>"
        return html
