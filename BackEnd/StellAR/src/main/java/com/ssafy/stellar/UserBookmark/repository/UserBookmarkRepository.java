package com.ssafy.stellar.UserBookmark.repository;

import com.ssafy.stellar.UserBookmark.entity.UserBookmarkEntity;
import com.ssafy.stellar.star.entity.StarEntity;
import com.ssafy.stellar.user.entity.UserEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Repository
public interface UserBookmarkRepository extends JpaRepository<UserBookmarkEntity, Long> {
    List<UserBookmarkEntity> findAllByUser(UserEntity user);

    UserBookmarkEntity findByUserAndStar(UserEntity user, StarEntity star);

//    UserBookmarkEntity findB

    @Transactional
    void deleteByUserAndStar(UserEntity user, StarEntity star);

}
