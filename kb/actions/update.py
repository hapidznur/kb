# -*- encoding: utf-8 -*-
# kb v0.1.5
# A knowledge base organizer
# Copyright © 2020, gnc.
# See /LICENSE for licensing information.

"""
kb update action module

:Copyright: © 2020, alshapton.
:License: GPLv3 (see /LICENSE).
"""

from typing import Dict
from pathlib import Path

import kb.db as db
from kb.db import get_artifact_by_id
from kb.entities.artifact import Artifact
import kb.filesystem as fs
import kb.initializer as initializer


def update_artifact(conn, old_artifact: Artifact, args: Dict[str, str], config: Dict[str, str], attachment):
    """
    Update artifact properties within the knowledge base of kb.

    Arguments:
    old_artifact:   - an object of type Artifact containing the old artifact details
    args:           - a dictionary containing the following fields:
                      id -> an id of an artifact - note - the ACTUAL db_id
                      title -> the title to be assigned to the artifact
                        to update
                      category -> the category to be assigned to the
                        artifact to update
                      tags -> the tags to be assigned to the artifact
                        to update
                      author -> the author to be assigned to the artifact
                        to update
                      status -> the status to be assigned to the artifact
                        to update
                      template -> the template to be assigned to the artifact
                        to update
    config:         - a configuration dictionary containing at least
                      the following keys:
                      PATH_KB_DB        - the database path of KB
                      PATH_KB_DATA      - the data directory of KB
                      PATH_KB_HIST      - the history menu path of KB
    attachment:     - new file content
"""
    initializer.init(config)

    template_name = args.get("template", "")
    updated_artifact = Artifact(
        id=None,
        title=args.get("title", old_artifact.title),
        category=args.get("category", old_artifact.category),
        tags=args.get("tags", old_artifact.tags),
        author=args.get("author", old_artifact.author),
        status=args.get("status", old_artifact.status),
        template=args.get("template", old_artifact.template),
        path=args.get("category", old_artifact.category) + '/' + args.get("title", old_artifact.title)
    )
    db.update_artifact_by_id(conn, old_artifact.id, updated_artifact)
    # If either title or category has been changed, we must move the file
    if args["category"] or args["title"]:
        old_category_path = Path(
            config["PATH_KB_DATA"],
            old_artifact.category)
        new_category_path = Path(
            config["PATH_KB_DATA"],
            args["category"] or old_artifact.category)
        fs.create_directory(new_category_path)

        fs.move_file(Path(old_category_path, old_artifact.title), Path(
            new_category_path, args["title"] or old_artifact.title))
        return -200
