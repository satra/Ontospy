#!/usr/bin/env python
# encoding: utf-8

# dumb script used to speed up testing


from ontospy import ontospy
import rdflib


if False:
	g = ontospy.Graph("ontospy/data/schemas/fabio.rdf")

	for x in g.classes:
		print x, x.count()


ontospy.viewCatalog()


# g = ontospy.Graph("http://dbpedia.org/sparql", endpoint=True)
# g = ontospy.Graph("http://factforge.net/sparql", endpoint=True)


# endpoints = ["http://uriburner.com/sparql", "http://www.w3.org/wiki/SparqlEndpoints", "http://data.semanticweb.org/sparql", "http://zbw.eu/beta/sparql/", "http://factforge.net/sparql", "http://sparql.vivo.ufl.edu/"]
#
#
#
# g = ontospy.SparqlEndpoint("http://factforge.net/sparql")