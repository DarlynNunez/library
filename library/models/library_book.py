# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    ######################
    # Private attributes #
    ######################
    _name = "library.book"
    _description = "Book"
    _order = "name"

    ###################
    # Default methods #
    ###################
    name = fields.Char(string="Name",
                       required=True)
    isbn_13 = fields.Char(string="ISBN 13",
                          required=True)

    ######################
    # Fields declaration #
    ######################
    author_id = fields.Many2one('res-partner',
                                string="Author_id",
                                required=True)

    category_id = fields.Many2many('library.book.category',
                                   string="Categories")


    ##############################
    # Compute and search methods #
    ##############################

    ############################
    # Constrains and onchanges #
    ############################

    #########################
    # CRUD method overrides #
    #########################

    ##################
    # Action methods #
    ##################

    ####################
    # Business methods #
    ####################
