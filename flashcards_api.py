#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""Flashcards API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""

# from __future__ import unicode_literals

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

package = 'Flashcards'


class VocabItem(messages.Message):
  """VocabItem that stores a message."""
  chineseChar = messages.StringField(1)
  chinesePinyin = messages.StringField(2)
  english = messages.StringField(3)


class VocabItemCollection(messages.Message):
  """Collection of VocabItems."""
  items = messages.MessageField(VocabItem, 1, repeated=True)


STORED_VOCAB_ITEMS = VocabItemCollection(items=[
    VocabItem(chineseChar=u'中国', chinesePinyin=u'Zhōng guó', english='China'),
    VocabItem(chineseChar=u'澳大利亚', chinesePinyin=u'Ào dà lì yǎ', english='Australia'),
    VocabItem(chineseChar=u'英国', chinesePinyin=u'Yīng guó', english='England'),
])


@endpoints.api(name='flashcards', version='v1')
class FlashcardsApi(remote.Service):
  """Flashcards API v1."""

  @endpoints.method(message_types.VoidMessage, VocabItemCollection,
                    path='vocabitem', http_method='GET',
                    name='vocabitem.listVocabItems')
  def vocab_items_list(self, unused_request):
    return STORED_VOCAB_ITEMS

  ID_RESOURCE = endpoints.ResourceContainer(
      message_types.VoidMessage,
      id=messages.IntegerField(1, variant=messages.Variant.INT32))

  @endpoints.method(ID_RESOURCE, VocabItem,
                    path='vocabitem/{id}', http_method='GET',
                    name='vocabitem.getVocabItems')
  def vocab_item_get(self, request):
    try:
      return STORED_VOCAB_ITEMS.items[request.id]
    except (IndexError, TypeError):
      raise endpoints.NotFoundException('Vocab Item %s not found.' %
                                        (request.id,))

APPLICATION = endpoints.api_server([FlashcardsApi])